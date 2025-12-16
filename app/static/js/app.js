// Глобальные переменные
let currentTest = null;
let currentAnswers = {};
let currentQuestionIndex = 0;

// Инициализация
document.addEventListener('DOMContentLoaded', function() {
    // Загружаем список тестов при загрузке страницы
    loadTests();

    // Обработчики кнопок
    document.getElementById('prevQuestionBtn')?.addEventListener('click', prevQuestion);
    document.getElementById('nextQuestionBtn')?.addEventListener('click', nextQuestion);
    document.getElementById('finishTestBtn')?.addEventListener('click', finishTest);
    document.getElementById('backToTestsBtn')?.addEventListener('click', showTestsList);
});

// Загрузка списка тестов
async function loadTests() {
    showLoading('tests-container');

    try {
        const response = await fetch('/api/tests');
        const data = await response.json();

        if (data.tests) {
            renderTestsList(data.tests);
        }
    } catch (error) {
        showError('tests-container', 'Ошибка загрузки тестов: ' + error.message);
    } finally {
        hideLoading('tests-container');
    }
}

// Отображение списка тестов
function renderTestsList(tests) {
    const container = document.getElementById('tests-container');
    if (!container) return;

    container.innerHTML = '';

    tests.forEach(test => {
        const testCard = document.createElement('div');
        testCard.className = 'col-md-6 col-lg-4';
        testCard.innerHTML = `
            <div class="card test-card h-100">
                <div class="card-header d-flex justify-content-between align-items-center">
                    <span>${test.name.split(' ')[0]}</span>
                    <span class="badge badge-test">${test.questions_count} вопросов</span>
                </div>
                <div class="card-body d-flex flex-column">
                    <h5 class="card-title">${test.name}</h5>
                    <p class="card-text flex-grow-1">${test.description}</p>
                    <div class="mt-auto">
                        <div class="d-flex justify-content-between align-items-center mb-2">
                            <small class="text-muted">Время: ${test.time_limit} мин</small>
                            <small class="text-muted">Баллы: ${test.min_score}-${test.max_score}</small>
                        </div>
                        <button class="btn btn-primary w-100" onclick="startTest('${test.code}')">
                            Начать тест
                        </button>
                    </div>
                </div>
            </div>
        `;
        container.appendChild(testCard);
    });
}

// Начать тест
async function startTest(testCode) {
    showLoading('tests-container');

    try {
        const response = await fetch(`/api/tests/${testCode}`);
        currentTest = await response.json();

        // Сбрасываем ответы
        currentAnswers = {};
        currentQuestionIndex = 0;

        // Показываем страницу теста
        showTestPage();
        renderQuestion();

    } catch (error) {
        showError('tests-container', 'Ошибка загрузки теста: ' + error.message);
    } finally {
        hideLoading('tests-container');
    }
}

// Показать страницу теста
function showTestPage() {
    document.getElementById('tests-page').classList.add('d-none');
    document.getElementById('test-page').classList.remove('d-none');
    document.getElementById('results-page').classList.add('d-none');

    // Устанавливаем заголовок теста
    if (currentTest) {
        document.getElementById('test-title').textContent = currentTest.name;
        document.getElementById('test-description').textContent = currentTest.description;
        document.getElementById('total-questions').textContent = currentTest.questions_count;
    }
}

// Отобразить вопрос
function renderQuestion() {
    if (!currentTest || !currentTest.questions) return;

    const question = currentTest.questions[currentQuestionIndex];
    const container = document.getElementById('test-questions');

    container.innerHTML = `
        <div class="test-question">
            <h5 class="mb-3">Вопрос ${question.question_number}: ${question.text}</h5>
            ${question.help_text ? `<p class="text-muted mb-3">${question.help_text}</p>` : ''}
            <div id="options-container">
                ${question.options.map(option => `
                    <div class="answer-option ${currentAnswers[question.id] === option.id ? 'selected' : ''}" 
                         onclick="selectOption(${question.id}, ${option.id})">
                        <div class="form-check">
                            <input class="form-check-input" type="radio" 
                                   name="question-${question.id}" 
                                   id="option-${option.id}"
                                   ${currentAnswers[question.id] === option.id ? 'checked' : ''}>
                            <label class="form-check-label" for="option-${option.id}">
                                ${option.text}
                            </label>
                        </div>
                    </div>
                `).join('')}
            </div>
        </div>
    `;

    updateProgress();
    updateNavigationButtons();
}

// Выбрать вариант ответа
function selectOption(questionId, optionId) {
    currentAnswers[questionId] = optionId;

    // Обновляем отображение
    const options = document.querySelectorAll('.answer-option');
    options.forEach(option => {
        option.classList.remove('selected');
    });

    const selectedOption = document.querySelector(`[onclick="selectOption(${questionId}, ${optionId})"]`);
    if (selectedOption) {
        selectedOption.classList.add('selected');
    }

    updateNavigationButtons();
}

// Обновить прогресс
function updateProgress() {
    const progress = ((currentQuestionIndex + 1) / currentTest.questions_count) * 100;
    document.getElementById('test-progress').style.width = `${progress}%`;
    document.getElementById('current-question').textContent = currentQuestionIndex + 1;
}

// Обновить кнопки навигации
function updateNavigationButtons() {
    const prevBtn = document.getElementById('prevQuestionBtn');
    const nextBtn = document.getElementById('nextQuestionBtn');
    const finishBtn = document.getElementById('finishTestBtn');

    prevBtn.disabled = currentQuestionIndex === 0;

    const currentQuestion = currentTest.questions[currentQuestionIndex];
    const hasAnswer = currentAnswers[currentQuestion.id];

    nextBtn.disabled = !hasAnswer;

    // Показывать кнопку завершения на последнем вопросе
    if (currentQuestionIndex === currentTest.questions_count - 1 && hasAnswer) {
        nextBtn.classList.add('d-none');
        finishBtn.classList.remove('d-none');
    } else {
        nextBtn.classList.remove('d-none');
        finishBtn.classList.add('d-none');
    }
}

// Следующий вопрос
function nextQuestion() {
    if (currentQuestionIndex < currentTest.questions_count - 1) {
        currentQuestionIndex++;
        renderQuestion();
    }
}

// Предыдущий вопрос
function prevQuestion() {
    if (currentQuestionIndex > 0) {
        currentQuestionIndex--;
        renderQuestion();
    }
}

// Завершить тест
async function finishTest() {
    // Преобразуем ответы в формат для API
    const answers = Object.entries(currentAnswers).map(([questionId, optionId]) => ({
        question_id: parseInt(questionId),
        selected_option_id: parseInt(optionId)
    }));

    showLoading('test-page');

    try {
        const response = await fetch(`/api/tests/${currentTest.code}/submit`, {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ answers })
        });

        const result = await response.json();

        if (result.success) {
            showResults(result);
        } else {
            throw new Error(result.error || 'Ошибка обработки результатов');
        }

    } catch (error) {
        showError('test-page', 'Ошибка отправки результатов: ' + error.message);
    } finally {
        hideLoading('test-page');
    }
}

// Показать результаты
function showResults(resultData) {
    document.getElementById('test-page').classList.add('d-none');
    document.getElementById('results-page').classList.remove('d-none');

    const result = resultData.result;

    // Заполняем результаты
    document.getElementById('results-test-name').textContent = resultData.test_name;
    document.getElementById('total-score').textContent = result.total_score;
    document.getElementById('severity-level').textContent = result.severity_level || result.risk_level || result.burnout_level || 'Н/Д';
    document.getElementById('interpretation-text').textContent = result.interpretation || 'Нет данных';

    // Рекомендации
    const recommendationsList = document.getElementById('recommendations-list');
    recommendationsList.innerHTML = '';

    if (result.recommendations && Array.isArray(result.recommendations)) {
        result.recommendations.forEach(rec => {
            const li = document.createElement('li');
            li.className = 'list-group-item';
            li.textContent = rec;
            recommendationsList.appendChild(li);
        });
    }

    // Обновляем дату
    const now = new Date();
    document.getElementById('results-date').textContent = now.toLocaleDateString('ru-RU');

    // Обновляем прогресс-бар
    const progressPercent = Math.min(100, (result.total_score / currentTest.max_score) * 100);
    document.getElementById('score-progress').style.width = `${progressPercent}%`;

    // Если есть субшкалы, показываем их
    if (result.subscale_scores && Object.keys(result.subscale_scores).length > 0) {
        showSubscales(result.subscale_scores);
    }
}

// Показать субшкалы
function showSubscales(subscales) {
    const container = document.getElementById('subscales-container');
    if (!container) return;

    let html = '<h6 class="mt-4">Результаты по субшкалам:</h6><div class="row">';

    Object.entries(subscales).forEach(([name, score]) => {
        html += `
            <div class="col-md-4 mb-3">
                <div class="card">
                    <div class="card-body p-3">
                        <h6 class="card-subtitle mb-2 text-muted">${name}</h6>
                        <div class="display-6 fw-bold">${score}</div>
                    </div>
                </div>
            </div>
        `;
    });

    html += '</div>';
    container.innerHTML = html;
}

// Вернуться к списку тестов
function showTestsList() {
    document.getElementById('tests-page').classList.remove('d-none');
    document.getElementById('test-page').classList.add('d-none');
    document.getElementById('results-page').classList.add('d-none');

    // Перезагружаем список тестов
    loadTests();
}

// Утилиты
function showLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        const spinner = element.querySelector('.loading-spinner') || createSpinner();
        spinner.style.display = 'block';
        element.appendChild(spinner);
    }
}

function hideLoading(elementId) {
    const element = document.getElementById(elementId);
    if (element) {
        const spinner = element.querySelector('.loading-spinner');
        if (spinner) spinner.style.display = 'none';
    }
}

function createSpinner() {
    const spinner = document.createElement('div');
    spinner.className = 'loading-spinner';
    spinner.innerHTML = `
        <div class="spinner-border text-primary" role="status">
            <span class="visually-hidden">Загрузка...</span>
        </div>
        <p class="mt-2">Загрузка...</p>
    `;
    return spinner;
}

function showError(elementId, message) {
    const element = document.getElementById(elementId);
    if (element) {
        const errorDiv = document.createElement('div');
        errorDiv.className = 'error-message';
        errorDiv.innerHTML = `
            <strong>Ошибка!</strong> ${message}
            <button type="button" class="btn-close float-end" onclick="this.parentElement.remove()"></button>
        `;
        element.prepend(errorDiv);
    }
}

// Экспортируем функции для использования в HTML
window.loadTests = loadTests;
window.startTest = startTest;
window.selectOption = selectOption;
window.nextQuestion = nextQuestion;
window.prevQuestion = prevQuestion;
window.finishTest = finishTest;
window.showTestsList = showTestsList;