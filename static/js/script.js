
$(document).ready(function() {
    $('#prediction-form').submit(function(event) {
        event.preventDefault();

        var formData = {
            'temp': $('#temp').val(),
            'RH': $('#RH').val(),
            'wind': $('#wind').val()
        };

        $.ajax({
            type: 'POST',
            url: '/predict',
            contentType: 'application/json',
            data: JSON.stringify(formData),
            success: function(response) {
                var resultText = 'Prediction: ' + (response.fire ? 'Forest fire will occur' : 'No forest fire') + '<br>';
                resultText += 'Probability: ' + (response.probability[1] * 100).toFixed(2) + '%<br>';
                resultText += 'Model Accuracy: ' + (response.accuracy * 100).toFixed(2) + '%';
                $('#result').html(resultText);
            },
            error: function(error) {
                console.log(error);
                $('#result').text('Error occurred while predicting.');
            }
        });
    });
});
