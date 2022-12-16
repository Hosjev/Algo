interface Product {
    id: number;
    description: string;
}

class ProdService {
    getProds(description: string): Product[];
    getProds(id: number): Product;
    getProds(product: number | string): Product[] | Product {
        if (typeof product === "string") {
            console.log(`Hit string type on ${product}, returning`);
            return [{ id: 145, description: 'thing' }];
        } else if (typeof product === "number") {
            console.log(`Hit number type on ${product}, returning`);
            return { id: product, description: 'pants' };
        }

    }
}

const item: ProdService = new ProdService();
console.log(item.getProds('shirt'));
console.log(item.getProds(123));