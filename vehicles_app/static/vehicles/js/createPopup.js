function submitVehicleForm(event) {
    event.preventDefault(); // 폼의 기본 제출 동작을 막음

    var form = document.getElementById('vehicleForm');
    var formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData,
        headers: {
            'X-CSRFToken': document.querySelector('[name=csrfmiddlewaretoken]').value
        }
    })
    .then(response => {
        if (response.ok) {
            return response.json();
        } else {
            return response.json().then(err => { throw err });
        }
    })
    .then(data => {
        alert(data.message);
        window.location.reload();  // 페이지를 리로드해서 테이블을 업데이트합니다.
    })
    .catch(error => {
        console.error('Error:', error);
        alert('Error: ' + JSON.stringify(error.errors));
    });
}

function openCreatePopup() {
    document.getElementById('createPopup').style.display = 'block';
}

function closeCreatePopup() {
    document.getElementById('createPopup').style.display = 'none';
}

// DOMContentLoaded 이벤트에서 이벤트 리스너를 등록합니다.
document.addEventListener('DOMContentLoaded', function() {
    document.querySelector('.vehicleCreateButton').addEventListener('click', submitVehicleForm);
});
