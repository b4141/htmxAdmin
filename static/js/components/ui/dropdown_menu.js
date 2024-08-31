function dropDownClickShowHide(event) {
  if (event.target.parentElement.querySelector('.ui-dropdown-menu-content').classList.contains('show')) {
    closeAllDropDowns();
  } else {
    closeAllDropDowns();
    event.target.parentElement.querySelector('.ui-dropdown-menu-content').classList.add('show');
  }
}

function closeAllDropDowns() {
  let dropDowns = document.getElementsByClassName('ui-dropdown-menu-content');
  for (let dropDown of dropDowns) {
    if (dropDown.classList.contains('show')) {
      dropDown.classList.remove('show');
    }
  }
}

function handleWindowClickForDropDown(event) {
  if (event.target.hasAttribute("dropDownPreventClose")) {
    return;
  }
  if (!event.target.parentElement.classList.contains("ui-dropdown-menu")) {
    closeAllDropDowns();
  }
}
