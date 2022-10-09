import { Injectable } from '@angular/core';
import { LoginInterface } from '../models/login.interface';
import { ResponseInterface } from '../models/response.interface';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import { map, switchMap } from 'rxjs/operators';
import { timer } from 'rxjs';

const TIME=5000; //milisegundos

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseUrl = "http://127.0.0.1:5000/api";
  constructor(private http:HttpClient) { }

  login(form):Observable<ResponseInterface>{
    let route = `${this.baseUrl}/users/login`;
    return this.http.post<ResponseInterface>(route, form);
  }

  //Usuarios
  getUserByEmail(email:string):Observable<any> {
    let route = `${this.baseUrl}/users/getUserByEmail/${email}`;
    return this.http.get(route);
  }

  //Carpetas
  getAllFoldersByIdPanel(id_panel:number, id_owner:number):Observable<any> {
    let route = `${this.baseUrl}/folders/getAllByIdPanel/${id_owner}/${id_panel}`;
    return this.http.get(route);
  }

  addFolder(id_editor:number):Observable<any> {
    let body = {
      'name': `Nueva carpeta ${this.formatDate()}`,
      'editor': id_editor
    }
    let route = `${this.baseUrl}/folders/add`;
    return this.http.post(route, body);
  }
  
  //Borrar arpeta por ID
  deleteFolderById(id_folder:number):Observable<any> {
    let id_owner = localStorage.getItem("ID");
    let route = `${this.baseUrl}/folders/delete/${id_owner}/${id_folder}`;
    return this.http.delete(route);
  }

  //Notas
  addNote(id_folder:number, id_editor:number):Observable<any> {
    let body = {
      'name': `Nueva nota ${this.formatDate()}`,
      'description': '',
      'parentFolder': id_folder,
      'lastEditor': id_editor
    }
    let route = `${this.baseUrl}/notes/add`;
    return this.http.post(route, body);
  }

  updateNote(id_note:any, note:any):Observable<any>{
    let body = {
      'name': note.name,
      'description': note.description,
      'parentFolder': note.parentFolder,
      'lastEditor': note.lastEditor,
      'panel': note.panel
    }
    let route = `${this.baseUrl}/notes/update/${id_note}`;
    return this.http.put(route, body);
  }

  // formatear fecha para nombre de nota
  formatDate(){
    let today = new Date()
    let day:any, month:any, year:any;
    day = today.getDate();
    month = today.getMonth() + 1;
    year = today.getFullYear();
    day < 10 ? day = '0' + day : day;
    month < 10 ? month = '0' + month : month;
    return `${day}/${month}/${year}`;
  }

  //Buscador
  getNotesByContent(content:any, id:any):Observable<any>{
    let body = {'content': content, "id_user": id}
    let route = `${this.baseUrl}/notes/search`;
    return this.http.post(route, body);
  }
}