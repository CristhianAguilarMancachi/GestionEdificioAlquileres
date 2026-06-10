import { ComponentFixture, TestBed } from '@angular/core/testing';

import { Oficinas } from './oficinas';

describe('Oficinas', () => {
  let component: Oficinas;
  let fixture: ComponentFixture<Oficinas>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [Oficinas],
    }).compileComponents();

    fixture = TestBed.createComponent(Oficinas);
    component = fixture.componentInstance;
    await fixture.whenStable();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
