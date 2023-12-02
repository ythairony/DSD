import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { LanchesComponent } from './lanches/lanches.component';
import { BebidasComponent } from './bebidas/bebidas.component';
import { DocesComponent } from './doces/doces.component';

@NgModule({
  declarations: [
    AppComponent,
    LanchesComponent,
    BebidasComponent,
    DocesComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
