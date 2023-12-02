import { Component } from '@angular/core';
import { DocesService } from '../doces.service';
import { Item } from '../item';

@Component({
  selector: 'app-doces',
  templateUrl: './doces.component.html',
  styleUrls: ['./doces.component.css']
})
export class DocesComponent {
  itens: Item[] = []
  
  constructor(private service: DocesService) {
  }

  ngOnInit(): void {
    this.service.getDoces().subscribe(data => this.itens = data);
  }
}
