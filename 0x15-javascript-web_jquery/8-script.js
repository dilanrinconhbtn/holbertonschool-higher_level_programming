$.get('https://swapi.co/api/films/?format=json', function (data) {
  const a = data.results;
  for (let i = 0; i < a.length; i++) {
    $('UL#list_movies').append('<li>' + a[i].title + '</li>');
  }
});
