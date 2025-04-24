async function sendMessage() {
    const userInput = document.getElementById('userInput').value;
    if (!userInput) {
        alert('질문을 입력해주세요.');
        return;
    }

    const responseArea = document.getElementById('responseArea');
    responseArea.innerHTML = '로딩 중...';

    try {
        const response = await fetch('http://localhost:8000/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ prompt: userInput }),
        });

        if (!response.ok) {
            throw new Error('네트워크 응답에 문제가 있습니다.');
        }

        const data = await response.json();
        responseArea.innerHTML = `<p>${data.response}</p>`;
    } catch (error) {
        console.error('오류:', error);
        responseArea.innerHTML = '<p>응답을 가져오는 데 실패했습니다. 다시 시도해주세요.</p>';
    }

    document.getElementById('userInput').value = '';
}
