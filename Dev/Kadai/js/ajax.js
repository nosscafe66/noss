$(function () {
  $.ajax({
    url: './test.py',
    type: 'post',
    data: { data: 'テスト' }
  }).done(function (data) {
    console.log(data);
  }).fail(function () {
    console.log('failed');
  });
});