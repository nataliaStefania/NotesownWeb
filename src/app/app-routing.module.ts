import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { FoldersComponent } from './components/folders/folders.component';
import { EditorComponent } from './pages/editor/editor.component';
import { LoginComponent } from './pages/login/login.component';
import { NotFoundComponent } from './pages/not-found/not-found.component';
import { RegisterComponent } from './pages/register/register.component';

const routes: Routes = [
  { path: '',   redirectTo: 'login', pathMatch: 'full' }, // redirect to `first-component`
  { path: 'editor', component: EditorComponent },
  { path: 'login', component: LoginComponent },
  { path: 'register', component: RegisterComponent },
  { path: '404', component: NotFoundComponent },
  //{ path: '500', component: InternalServerComponent }, 
  { path: '**', redirectTo: '/404', pathMatch: 'full' },
  { path: 'folders', component: FoldersComponent },
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
export const RoutingComponents = [ EditorComponent, LoginComponent, NotFoundComponent, RegisterComponent]