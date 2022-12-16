var AppState = /** @class */ (function () {
    function AppState() {
        this.counter = 0;
    }
    AppState.getInstance = function () {
        if (AppState.instanceRef === undefined) {
            AppState.instanceRef = new AppState();
        }
        return AppState.instanceRef;
    };
    return AppState;
}());
