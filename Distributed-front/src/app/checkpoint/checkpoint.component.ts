import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-checkpoint',
  templateUrl: './checkpoint.component.html',
  styleUrls: ['./checkpoint.component.css']
})
export class CheckpointComponent {
  userId: string = '';
   /* constructor(private http: HttpClient) { } */
  onCheckpointoldUser() {

    const oldUser = { userId:this.userId,username: 'JohnDoe', password: 'mysecret' };
/*     this.http.post('http://localhost:3000/users', newUser).subscribe(response => {
      console.log(response);
    }); */
print()
  }
}
