import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Item } from './item';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class DocesService {
  url = 'http://localhost:10000/gateway/';

  constructor(private http: HttpClient) { }

  getDoces():Observable<Item[]> {
    return this.http.get<Item[]>(this.url + 'doces/')
  }
}
