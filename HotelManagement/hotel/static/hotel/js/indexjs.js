$(document).ready(function () {
  var currentIndex = 0;
  var items = $(".image-container img");
  var itemAmt = items.length;

  function cycleItems() {
    var item = $(".image-container img").eq(currentIndex);
    items.hide();
    item.css("display", "inline-block");
  }

  var autoSlide = setInterval(function () {
    currentIndex += 1;
    if (currentIndex > itemAmt - 1) {
      currentIndex = 0;
    }
    cycleItems();
  }, 3000);

  $(".next").click(function () {
    clearInterval(autoSlide);
    currentIndex += 1;
    if (currentIndex > itemAmt - 1) {
      currentIndex = 0;
    }
    cycleItems();
  });

  $(".prev").click(function () {
    clearInterval(autoSlide);
    currentIndex -= 1;
    if (currentIndex < 0) {
      currentIndex = itemAmt - 1;
    }
    cycleItems();
  });
});

function delete_section_fun() {
  document.getElementById("insert_section").style.display = "none";
  document.getElementById("update_section").style.display = "none";
  document.getElementById("view_section").style.display = "none";
  document.getElementById("delete_section").style.display = "block";

  // console.log(data);
}
function update_section_fun() {
  console.log(document.getElementById("insert_section"));
  document.getElementById("insert_section").style.display = "none";
  document.getElementById("update_section").style.display = "block";
  document.getElementById("view_section").style.display = "none";
  document.getElementById("delete_section").style.display = "none";

  // console.log(data);
}
function view_section_fun() {
  document.getElementById("insert_section").style.display = "none";
  document.getElementById("update_section").style.display = "none";
  document.getElementById("view_section").style.display = "block";
  document.getElementById("delete_section").style.display = "none";

  // console.log(data);
}
function insert_section_fun() {
  document.getElementById("insert_section").style.display = "block";
  document.getElementById("update_section").style.display = "none";
  document.getElementById("view_section").style.display = "none";
  document.getElementById("delete_section").style.display = "none";

  // console.log(data);
}

console.log("hello");
console.log("This is indexjs file");

function room_type_a_fun() {
  console.log("helo");
  document.getElementById("room_type_a_booking").style.display = "block";
  document.getElementById("list_room_a").style.backgroundColor =
    "rgb(108, 108, 207)";
  document.getElementById("room_type_b_booking").style.display = "none";
  document.getElementById("list_room_b").style.backgroundColor = "#333";
  document.getElementById("room_type_c_booking").style.display = "none";
  document.getElementById("list_room_c").style.backgroundColor = "#333";
}

function room_type_b_fun() {
  console.log("helo");
  document.getElementById("room_type_a_booking").style.display = "none";
  document.getElementById("list_room_a").style.backgroundColor = "#333";

  document.getElementById("room_type_b_booking").style.display = "block";
  document.getElementById("list_room_b").style.backgroundColor =
    "rgb(108, 108, 207)";

  document.getElementById("room_type_c_booking").style.display = "none";
  document.getElementById("list_room_c").style.backgroundColor = "#333";
}

function room_type_c_fun() {
  console.log("helo");
  document.getElementById("room_type_a_booking").style.display = "none";
  document.getElementById("list_room_a").style.backgroundColor = "#333";

  document.getElementById("room_type_b_booking").style.display = "none";
  document.getElementById("list_room_b").style.backgroundColor = "#333";

  document.getElementById("room_type_c_booking").style.display = "block";
  document.getElementById("list_room_c").style.backgroundColor =
    "rgb(108, 108, 207)";
}

function makevisibleSubmit() {
  console.log("hello");
  document.getElementById("InsertFinalSubmitButton").style.display = "block";
}

function hello() {
  console.log("hello nitin");
}

console.log("Hello");
