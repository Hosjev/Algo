abstract class CompanyWorker {
    constructor(public name: string) {}

    changeAddr(newAddr: string) {
        console.log(`Changing addr to ${newAddr}`);
    }

    giveDayOff() {
        console.log(`Giving day off to ${this.name}`);
    }

    promote(percent: number) {
        this.giveDayOff();
        this.increasePay(percent);
    }

    abstract increasePay(percent: number): void;
}

class Employee extends CompanyWorker {
    increasePay(percent: number): void {
        console.log(`Increasing salary for ${this.name} by ${percent}`);
    }
}

class Contractor extends CompanyWorker {
    increasePay(percent: number): void {
        console.log(`Increasing hourly for ${this.name} by ${percent}`);
    }
}


const workers: CompanyWorker[] = [];

workers.push(new Employee('Jane'));
workers.push(new Contractor('Fran'));

workers.forEach(element => {
    element.promote(50);
});