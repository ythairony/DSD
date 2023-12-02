import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { LanchesComponent } from './lanches/lanches.component';
import { BebidasComponent } from './bebidas/bebidas.component';
import { DocesComponent } from './doces/doces.component';

const routes: Routes = [
  { path: "lanches", component: LanchesComponent },
  { path: "bebidas", component: BebidasComponent },
  { path: "doces", component: DocesComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
