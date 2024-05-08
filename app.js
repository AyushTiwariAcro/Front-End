$(document).ready(function () {
    // Fetch supported languages and populate dropdowns
    $.get('https://rapidapi.p.rapidapi.com/languages', function (data) {
        const languages = data.data.languages;
        const sourceSelect = $('#source');
        const targetSelect = $('#target');
        
        languages.forEach(lang => {
            sourceSelect.append(<option value="${lang.language}">${lang.name}</option>);
            targetSelect.append(<option value="${lang.language}">${lang.name}</option>);
        });
    });

    $('#translateBtn').click(function () {
        const text = $('#text').val();
        const source = $('#source').val();
        const target = $('#target').val();

        $.post('/translate', { text: text, source: source, target: target }, function (data) {
            $('#output').text(data.translatedText);
        });
    });
});