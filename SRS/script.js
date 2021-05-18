var elm = document.querySelector('#sidenav');
var ms = new MenuSpy(elm);

var ms = new MenuSpy(elm, {

    // menu selector
    menuItemSelector: 'a[href^="#"]',

    // CSS class for active item
    activeClass: 'active',

    // amount of space between your menu and the next section to be activated.
    threshold: 0,

    // enable or disable browser's hash location change.
    enableLocationHash: true,

    // timeout to apply browser's hash location.
    hashTimeout: 600,

    // called every time a new menu item activates.
    callback: null

});