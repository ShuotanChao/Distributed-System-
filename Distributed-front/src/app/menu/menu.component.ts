import { Component } from '@angular/core';
import { ProductChooseComponent } from '../product-choose/product-choose.component';
import { CreateUserComponent } from '../create-user/create-user.component';
import { CheckpointComponent } from '../checkpoint/checkpoint.component';

@Component({
  selector: 'app-menu',
  templateUrl: './menu.component.html',
  styleUrls: ['./menu.component.css']
})
export class MenuComponent {
  showProductChoose: boolean = false;
  showCreatuser: boolean = false;
  showCheckpoint: boolean = false;

  onShowProductChoose() {
    this.showProductChoose = !this.showProductChoose;
  }
  onShowCreateuser(){
    this.showCreatuser = !this.showCreatuser;
  }
  onShowCheckpoint(){
    this.showCheckpoint=!this.showCheckpoint;
  }
}
