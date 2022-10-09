import { Directive, ViewContainerRef } from '@angular/core';

@Directive({
  selector: '[dynamicMenu]'
})
export class DynamicMenuDirective {
  constructor(public viewContainerRef:ViewContainerRef) { }
}
