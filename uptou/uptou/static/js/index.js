$("#searchbtn").click(function() {
  // value値を取得
   const str1 = $("#station").val();
  $("#text1").val(str1);
});

// function getLocation() {
//   var line = $('#line').val();
//   var name = $('#station').val();
//   // 経度
//   var lon;
//   // 緯度
//   var lat;

//   var url = 'http://express.heartrails.com/api/json?method=getStations&line='+line+'&name='+name;
//   $.getJSON(url,
//   )
//   // 結果を取得したら…
//   .done(function(response) {
//     if (response.response.station[0]) {
//       lat = response.response.station[0].x;
//       lon = response.response.station[0].y;
//     } 
//   });

//   list = [lat, lon];

//   return list;
// }

function submitButton(){
  $('#id_line').val($('#line').val());
  $('#id_station').val($('#station').val());
  $('#id_category').val($('#category').val());
  $('#id_radius').val($('#radius').val());
  $('#id_keyword').val($('#keyword').val());
  $('form').submit();
}
