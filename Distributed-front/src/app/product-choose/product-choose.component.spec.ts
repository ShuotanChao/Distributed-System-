import { ComponentFixture, TestBed } from '@angular/core/testing';

import { ProductChooseComponent } from './product-choose.component';

describe('ProductChooseComponent', () => {
  let component: ProductChooseComponent;
  let fixture: ComponentFixture<ProductChooseComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ ProductChooseComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(ProductChooseComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
