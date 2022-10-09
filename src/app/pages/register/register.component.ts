import { Component, OnInit } from '@angular/core';
import { Output, EventEmitter } from '@angular/core';
import { FormGroup, FormControl, Validators } from '@angular/forms';
import { ApiService } from 'src/app/services/api.service';
import { LoginInterface } from 'src/app/models/login.interface';
import { ResponseInterface } from 'src/app/models/response.interface';
import { Router } from '@angular/router';

@Component({
  selector: 'app-register',
  templateUrl: './register.component.html',
  styleUrls: ['./register.component.scss']
})
export class RegisterComponent implements OnInit {
  loginForm = new FormGroup({
    email : new FormControl('', Validators.required),
    password : new FormControl('', Validators.required)
  })
  @Output() sesion = new EventEmitter<boolean>();
  errorStatus:boolean = false;
  errorMsj:string;

  constructor(private api:ApiService, private router:Router) { }

  ngOnInit(): void {
    this.validateSesion()
  }

  validateSesion(){
    if(localStorage.getItem("sesion")){
      this.router.navigate(['editor'])
    }
  }
  onLogin(form){
    this.api.login(form).subscribe(data =>{
      let dataResponse:ResponseInterface = data;
      if(dataResponse.status == "ok"){
        localStorage.setItem("sesion", dataResponse.response);
        this.getUserByEmail(form['email'])
        this.router.navigate(['editor'])
      } else{
        this.errorStatus = true;
        this.errorMsj = dataResponse.response;
      }
    });
  }

  getUserByEmail(email:string){
    this.api.getUserByEmail(email).subscribe(data =>{
      let user = {
        "id": data.id,
        "name": data.name,
        "lastname": data.lastname,
        "email": data.email,
      }
      localStorage.setItem("username", `${user.name} ${user.lastname}`);
      localStorage.setItem("ID", user.id);
    });
  }

  stateSesionChange() {
    this.sesion.emit(true);
  }
}
