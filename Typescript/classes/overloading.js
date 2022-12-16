var ProdService = /** @class */ (function () {
    function ProdService() {
    }
    ProdService.prototype.getProds = function (product) {
        if (typeof product === "string") {
            console.log("Hit string type on " + product + ", returning");
            return [{ id: 145, description: 'thing' }];
        }
        else if (typeof product === "number") {
            console.log("Hit number type on " + product + ", returning");
            return { id: product, description: 'pants' };
        }
    };
    return ProdService;
}());
var item = new ProdService();
console.log(item.getProds('shirt'));
console.log(item.getProds(123));
