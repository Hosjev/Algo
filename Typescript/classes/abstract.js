var __extends = (this && this.__extends) || (function () {
    var extendStatics = function (d, b) {
        extendStatics = Object.setPrototypeOf ||
            ({ __proto__: [] } instanceof Array && function (d, b) { d.__proto__ = b; }) ||
            function (d, b) { for (var p in b) if (b.hasOwnProperty(p)) d[p] = b[p]; };
        return extendStatics(d, b);
    };
    return function (d, b) {
        extendStatics(d, b);
        function __() { this.constructor = d; }
        d.prototype = b === null ? Object.create(b) : (__.prototype = b.prototype, new __());
    };
})();
var CompanyWorker = /** @class */ (function () {
    function CompanyWorker(name) {
        this.name = name;
    }
    CompanyWorker.prototype.changeAddr = function (newAddr) {
        console.log("Changing addr to " + newAddr);
    };
    CompanyWorker.prototype.giveDayOff = function () {
        console.log("Giving day off to " + this.name);
    };
    CompanyWorker.prototype.promote = function (percent) {
        this.giveDayOff();
        this.increasePay(percent);
    };
    return CompanyWorker;
}());
var Employee = /** @class */ (function (_super) {
    __extends(Employee, _super);
    function Employee() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Employee.prototype.increasePay = function (percent) {
        console.log("Increasing salary for " + this.name + " by " + percent);
    };
    return Employee;
}(CompanyWorker));
var Contractor = /** @class */ (function (_super) {
    __extends(Contractor, _super);
    function Contractor() {
        return _super !== null && _super.apply(this, arguments) || this;
    }
    Contractor.prototype.increasePay = function (percent) {
        console.log("Increasing hourly for " + this.name + " by " + percent);
    };
    return Contractor;
}(CompanyWorker));
var workers = [];
workers.push(new Employee('Jane'));
workers.push(new Contractor('Fran'));
workers.forEach(function (element) {
    element.promote(50);
});
