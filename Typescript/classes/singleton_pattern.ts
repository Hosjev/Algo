class AppState {
    counter = 0;
    private static instanceRef: AppState;

    private constructor() {}
    
    static getInstance(): AppState {
        if (AppState.instanceRef === undefined) {
            AppState.instanceRef = new AppState();
        }
        return AppState.instanceRef;
    }
}