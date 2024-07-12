function goBack() {
    window.history.back();
}

function navigateTo(page) {
    switch (page) {
        case 'index':
            window.location.href = 'index.html';
            break;
        case 'C++':
            window.location.href = 'C++.html';
            break;
        case 'python':
            window.location.href = 'python.html';
            break;
        case 'css':
            window.location.href = 'css.html';
            break;
        case 'lan':
             window.location.href = 'lan.html';
             break;
        case 'return':
             window.location.href = 'return.html';
             break;     
        case 'end':
            window.location.href = 'end.html';
            break;          
        default:
            break;
    }
}

function showAnswer(id) {
    var answer = document.getElementById(id);
    if (answer.style.display === "none") {
        answer.style.display = "block";
    } else {
        answer.style.display = "none";
    }
}

function checkAnswer(textareaId, answerId, correctAnswer) {
    var userAnswer = document.getElementById(textareaId).value.trim();
    var answerElement = document.getElementById(answerId);
    if (userAnswer === correctAnswer) {
        answerElement.innerHTML = "正确";
        answerElement.style.color = "green";
    } else {
        answerElement.innerHTML = "错误，正确答案是:<br>" + correctAnswer;
        answerElement.style.color = "red";
    }
    answerElement.style.display = "block";
}

