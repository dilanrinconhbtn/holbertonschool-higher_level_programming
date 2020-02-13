$.get('https://fourtonfish.com/hellosalut/?lang=fr', function (data) {
  $('DIV#hello').append('<li>' + data.hello + '</li>');
});
