import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule, RoutingComponents } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavComponent } from './components/nav/nav.component';
import { FooterComponent } from './components/footer/footer.component';
import { SharedComponent } from './components/shared/shared.component';
import { ArchivedComponent } from './components/archived/archived.component';
import { PinnedComponent } from './components/pinned/pinned.component';
import { FoldersComponent } from './components/folders/folders.component';
import { ContextualMenuComponent } from './components/contextual-menu/contextual-menu.component';
import { DynamicMenuDirective } from './directives/dynamic-menu.directive';
import { ReactiveFormsModule, FormsModule } from '@angular/forms';
import { HttpClientModule } from '@angular/common/http';
import { CKEditorModule } from '@ckeditor/ckeditor5-angular';

@NgModule({
  declarations: [
    AppComponent,
    NavComponent,
    FooterComponent,
    SharedComponent,
    ArchivedComponent,
    PinnedComponent,
    FoldersComponent,
    RoutingComponents,
    ContextualMenuComponent,
    DynamicMenuDirective,
    
  ],
  imports: [
    CKEditorModule,
    ReactiveFormsModule,
    FormsModule,
    HttpClientModule,
    AppRoutingModule,
    BrowserModule,
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
