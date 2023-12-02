import { Component } from '@angular/core';
import { LanchesService } from '../lanches.service';
import { Item } from '../item';

@Component({
  selector: 'app-lanches',
  templateUrl: './lanches.component.html',
  styleUrls: ['./lanches.component.css']
})
export class LanchesComponent {
  itens: Item[] = []
  
  constructor(private service: LanchesService) {
  }

  ngOnInit(): void {
    this.service.getLanches().subscribe(data => this.itens = data);
  }
}
