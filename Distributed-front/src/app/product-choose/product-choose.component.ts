import { Component } from '@angular/core';

@Component({
  selector: 'app-product-choose',
  templateUrl: './product-choose.component.html',
  styleUrls: ['./product-choose.component.css']
})
export class ProductChooseComponent {
  products: Product[] = [
    { name: 'Latte', imageUrl: 'assets/latte.webp', description: 'good Latte', price: 3.99 },
    { name: 'Espresso', imageUrl: 'assets/Espresso.jpg', description: 'good Espresso', price: 4.99 },
    { name: 'Americano', imageUrl: 'assets/Americano.jpg', description: 'good Americano', price: 5.99 }
  ];
}
interface Product {
  name: string;
  imageUrl: string;
  description: string;
  price: number;
}

