var UserRole;
(function (UserRole) {
    UserRole["Administrator"] = "admin";
    UserRole["Developer"] = "devel";
})(UserRole || (UserRole = {}));
function loadUser() {
    return JSON.parse('{"name": "Wend", "role": "devel"}');
}
var user = loadUser();
switch (user.role) {
    case UserRole.Administrator:
        console.log('User gets full Control Panel');
        break;
    case UserRole.Developer:
        console.log('User gets limited Control Panel');
        break;
}
