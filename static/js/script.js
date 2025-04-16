$(document).ready(function() {
    $('#user-input').keypress(function(e) {
      if (e.which === 13) {
        let message = $(this).val();
        $('#chat-box').append(`<div><strong>Toi:</strong> ${message}</div>`);
        $(this).val('');
  
        $.ajax({
          type: 'POST',
          url: '/chat',
          contentType: 'application/json',
          data: JSON.stringify({ message: message }),
          success: function(data) {
            $('#chat-box').append(`<div><strong>IA:</strong> ${data.reply}</div>`);
            $('#chat-box').scrollTop($('#chat-box')[0].scrollHeight);
          }
        });
      }
    });
  });
  