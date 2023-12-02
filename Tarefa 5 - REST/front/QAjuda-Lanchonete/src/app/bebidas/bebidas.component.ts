import { Component } from '@angular/core';
import { BebidasService } from '../bebidas.service';
import { Item } from '../item';

@Component({
  selector: 'app-bebidas',
  templateUrl: './bebidas.component.html',
  styleUrls: ['./bebidas.component.css']
})
export class BebidasComponent {
  itens: Item[] = []
  
  constructor(private service: BebidasService) {
  }

  ngOnInit(): void {
    this.service.getBebidas().subscribe(data => this.itens = data);
  }
}
