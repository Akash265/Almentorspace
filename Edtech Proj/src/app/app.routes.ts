import { Routes } from '@angular/router';
import { TextExtractorComponent } from './text-extractor/text-extractor.component';

export const routes: Routes = [
    { path: '', loadComponent: () => import('./text-extractor/text-extractor.component').then(c => c.TextExtractorComponent)},
];
