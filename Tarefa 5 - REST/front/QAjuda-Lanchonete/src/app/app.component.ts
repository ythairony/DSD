import { Component, OnInit } from '@angular/core';
import { Item } from './item';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';
import { LanchesService } from './lanches.service';
import { BebidasService } from './bebidas.service';
import { DocesService } from './doces.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit{
  title = 'QAjuda-Lanchonete';

  itens: Item[] = []
  
  constructor(private service: BebidasService) {
  }

  ngOnInit(): void {
    this.service.getBebidas().subscribe(data => this.itens = data);
  }
}
