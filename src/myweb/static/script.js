function goBack() {
    window.history.back();
}



function navigateTo(page) {
    
    switch (page) {
        case 'index':
            window.location.href = '{% url "index"%}';
            break;
        case 'C++':
            window.location.href = '{% url "C++"%}';
            break;
        case 'python':
            window.location.href = '{% url "python"%}';
            break;
        case 'css':
            window.location.href = '{% url "css"%}';
            break;
        case 'lan':
             window.location.href = '{% url "lan"%}';
             break;
        case 'return':
             window.location.href = '{% url "ret"%}';
             break;     
        case 'end':
            window.location.href = '{% url "end"%}';
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

