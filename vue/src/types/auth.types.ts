export interface DecodedUserToken {
  id: number;
  user_identifier: string;
  exp: number;
}

export interface UserToken {
  accessToken: string;
  tokenType: string;
}

export interface UserTokenResponse {
  access_token: string;
  token_type: string;
}
