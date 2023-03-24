import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-create-user',
  templateUrl: './create-user.component.html',
  styleUrls: ['./create-user.component.css']
})
export class CreateUserComponent {
  /* constructor(private http: HttpClient) { } */

  onCreateUser() {
    const newUser = { username: 'JohnDoe', password: 'mysecret' };
/*     this.http.post('http://localhost:3000/users', newUser).subscribe(response => {
      console.log(response);
    }); */
print()
  }
}
