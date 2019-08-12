/* Toggle between adding and removing the "responsive" class to navigation when the user clicks on the icon */
function toggleResponsiveNavBar() {
  const x = document.getElementById("myTopnav");
  if (x.className === "topnav") {
    x.className += " responsive";
  } else {
    x.className = "topnav";
  }
}