import { TestBed } from '@angular/core/testing';

import { LanchesService } from './lanches.service';

describe('LanchesService', () => {
  let service: LanchesService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(LanchesService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
