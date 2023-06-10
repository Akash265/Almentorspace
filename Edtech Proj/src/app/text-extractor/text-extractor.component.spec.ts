import { ComponentFixture, TestBed } from '@angular/core/testing';

import { TextExtractorComponent } from './text-extractor.component';

describe('TextExtractorComponent', () => {
  let component: TextExtractorComponent;
  let fixture: ComponentFixture<TextExtractorComponent>;

  beforeEach(() => {
    TestBed.configureTestingModule({
      imports: [TextExtractorComponent]
    });
    fixture = TestBed.createComponent(TextExtractorComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
