const btnSubmit = document.querySelector('#sub');
const displayOutput = document.querySelector('.output');

btnSubmit.addEventListener('click', () => {
    displayOutput.style.display = 'block';
    console.log('clicked...');
});
