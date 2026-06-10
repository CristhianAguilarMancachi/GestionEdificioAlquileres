import { ComponentFixture, TestBed } from '@angular/core/testing';

import { OficinaDetalle } from './oficina-detalle';

describe('OficinaDetalle', () => {
  let component: OficinaDetalle;
  let fixture: ComponentFixture<OficinaDetalle>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [OficinaDetalle],
    }).compileComponents();

    fixture = TestBed.createComponent(OficinaDetalle);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
