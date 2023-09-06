const moveablePic = document.getElementById('moveable-piv');
let  isDragging =false;

moveablePic.addEventListener('mousedown', (e) => {
    isDragging = true;
    moveablePic.style.cursor = 'grabbing';
});

document.addEventListener('mousemove',(e) => {
    if (!isDragging) return;
    const x = e.clientX;
    const y = e.clientY;
    moveablePic.style.left = x + 'px';
    moveablePic.style.top = y + 'px'; 
});

document.addEventListener('mouseup', () => {
    isDragging = false;
    moveablePic.style.cursor = 'grab';
})