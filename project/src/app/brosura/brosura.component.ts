import { Component } from '@angular/core';

@Component({
  selector: 'app-brosura',
  standalone: true,
  imports: [],
  templateUrl: './brosura.component.html',
  styleUrl: './brosura.component.scss'
})
export class BrosuraComponent {
  brosure: Brosura[] = [];


  constructor(private brosuraService: BrosuraService){}
  
  //u vreme incijializacije stranice
  ngOnInit(){
  
  this.fetchBrosure();
  console.log(this.brosure);
  
  
  }
  
  
  
  
  fetchBrosure(): void {
  
    this.brosuraService.getBrosure().subscribe(
    (data) => {
  
      this.brosure = data;
      console.log(this.brosure);
    },
    (error) => {
      console.log("Error fetching brosure:",error);
    }
  
  
  
    );
  
  
  
  
  }

}
