import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
// import {WebcamImage} from 'ngx-webcam'
// import {WebcamModule} from 'ngx-webcam';
import { createWorker } from 'tesseract.js';

@Component({
  selector: 'app-text-extractor',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './text-extractor.component.html',
  styleUrls: ['./text-extractor.component.css']
})
export class TextExtractorComponent {
    url = ""

    onselectFile(e: any) {
        if (e.target.files) {
            var reader = new FileReader();
            reader.readAsDataURL(e.target.files[0]);
            reader.onload = (event:any) => {
                this.url = event.target.result;
                console.log(this.url)
            }
        }
    }
    //TODO:the url can't be use for the OCR
    ocrResult = 'Recognizing...';
    constructor() {
      this.doOCR();
    }

    async doOCR() {
      const worker = await createWorker({
        logger: m => console.log(m),
      });
      await worker.loadLanguage('eng');
      await worker.initialize('eng');
      const { data: { text } } = await worker.recognize(this.url);
      this.ocrResult = text;
      console.log(text);
      await worker.terminate();
    }

    // webcamImage: WebcamImage | undefined
    // trigger: Subject<void> = new Subject<void>();

    // takeSnapshot(): void {
    //     this.trigger.next();
    // }
}
