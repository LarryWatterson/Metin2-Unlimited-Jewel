// find

							case ITEM_NEW_YEAR_GREETING_VNUM:

// add to top

							case 90028:
							{
								LPITEM item2;
// engelle
								if (!IsValidItemPosition(DestCell) || !(item2 = GetItem(DestCell)))
									return false;

								if (item2->IsExchanging() || item2->IsEquipped()) // her ihtimale karsi :)
									return false;

								if (item2->GetSocket() == 1){
									ChatPacket(CHAT_TYPE_INFO, LC_TEXT("zatesuresiz"));
								return false;}
// bb
								
								if (item2->GetType() == ITEM_ARMOR || item2->GetType() == ITEM_BELT)
								{
									item2->SetSocket(3,1);
									item2->SetSocket(2,0);
									item->SetCount(item->GetCount()-1);
									ChatPacket(CHAT_TYPE_INFO, LC_TEXT("suresizcevherok"));
								}
								
							}
								break;