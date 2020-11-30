$("#searchbtn").click(function() {
  // value値を取得
   const str1 = $("#station").val();
  $("#text1").val(str1);
});


function submitButton(){
  $('#id_station').val($('#station').val());
  $('#id_category').val($('#category').val());
  $('#id_radius').val(500);
  $('form').submit(
  //   function() {
  //       alert('in ajax');
  //       //event.preventDefault();
  //       var form = $(this);
  //       $.ajax({
  //         url: form.prop("action"),
  //         method: form.prop("method"),
  //         data: form.serialize(),
  //         timeout: 10000,
  //         dataType: "text",
  //       })
  //       .done( function(data) {
  //         alert("done");
  //         $("#selectedItem").text(data);
  //       })
  //       .fail(function(){
  //         alert('error');
  //       })
  //     }
  );
}
