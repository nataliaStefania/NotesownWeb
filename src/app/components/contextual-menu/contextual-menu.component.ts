import { Component, OnInit, Input, AfterViewInit, ViewChild, ElementRef} from '@angular/core';
import { ApiService } from 'src/app/services/api.service';

@Component({
  selector: 'app-contextual-menu',
  templateUrl: './contextual-menu.component.html',
  styleUrls: ['./contextual-menu.component.scss']
})
export class ContextualMenuComponent implements AfterViewInit {

  @Input() menuOptions:any;
  @ViewChild('menu') menu!: ElementRef;
  constructor(private api:ApiService) { }
  ngAfterViewInit(): void {
    let x = this.menuOptions[1]["x"];
    let y = this.menuOptions[1]["y"]
    this.menu.nativeElement.style.top = `${y + 10}px`;
    this.menu.nativeElement.style.left = `${x - 56}px`;
  }

  deleteFolder(id_folder:any, element:any){
    this.api.deleteFolderById(id_folder).subscribe( data =>{
      this.destroy(null, element);
    })
  }

  destroy(event:any, element){
    if(event == null || element == event.target){
      element.style.display = "none";

    }
  }
}
