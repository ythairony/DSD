import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Item } from './item';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';

@Injectable({
  providedIn: 'root'
})
export class LanchesService {
  url = 'http://localhost:10000/gateway/';

  constructor(private http: HttpClient) { }

  getLanches(): Observable<Item[]> {
    return this.http.get<Item[]>(this.url + 'lanches/');
  }
}
